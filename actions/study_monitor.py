import cv2
import cvzone
from cvzone.FaceMeshModule import FaceMeshDetector
from ultralytics import YOLO
import pygame
import os
import numpy as np
from pathlib import Path
from PyQt6.QtCore import QThread, pyqtSignal
from PyQt6.QtGui import QImage

class StudyMonitorThread(QThread):
    # Emit QImage so UI can render it natively
    frame_ready = pyqtSignal(QImage)
    status_updated = pyqtSignal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.running = True
        
        # Paths to assets
        self.base_dir = Path("assets/study").absolute()
        self.yolo_path = str(self.base_dir / "yolov8n.pt")
        self.alarm_path = str(self.base_dir / "alarm.mp3")
        self.facehide_path = str(self.base_dir / "faudio.mp3")
        self.phone_path = str(self.base_dir / "paudio.mp3")

    def run(self):
        # Initialize Pygame Mixer
        try:
            pygame.mixer.init()
            alarm_sleep = pygame.mixer.Sound(self.alarm_path)
            alarm_facehide = pygame.mixer.Sound(self.facehide_path)
            alarm_phone = pygame.mixer.Sound(self.phone_path)
        except Exception as e:
            print(f"[StudyMonitor] Audio init error: {e}")
            alarm_sleep = None
            alarm_facehide = None
            alarm_phone = None

        current_playing = None

        # Initialize Camera, Face Mesh, and YOLO Model
        cap = cv2.VideoCapture(0)
        face_detector = FaceMeshDetector(maxFaces=1)
        try:
            phone_detector = YOLO(self.yolo_path)
            classNames = phone_detector.names
        except Exception as e:
            print(f"[StudyMonitor] YOLO init error: {e}")
            phone_detector = None
            classNames = {}

        # Landmark Indices for Sleep Detection
        LEFT_EYE_TOP = 159
        LEFT_EYE_BOTTOM = 145
        FACE_LEFT = 130
        FACE_RIGHT = 243

        # Frame Counters & Thresholds
        closed_frames = 0
        SLEEP_THRESHOLD_FRAMES = 15

        covered_frames = 0
        COVER_THRESHOLD_FRAMES = 20

        self.status_updated.emit("Study Mode Active. Monitoring...")

        while self.running:
            success, img = cap.read()
            if not success:
                break

            is_audio_busy = pygame.mixer.get_busy() if pygame.mixer.get_init() else False

            if not is_audio_busy:
                current_playing = None

            # 1. SLEEP & FACE COVER DETECTION
            img, faces = face_detector.findFaceMesh(img, draw=False)
            is_sleepy = False
            is_face_covered = False

            if faces:
                covered_frames = 0
                face = faces[0]

                eye_dist, _ = face_detector.findDistance(face[LEFT_EYE_TOP], face[LEFT_EYE_BOTTOM])
                face_dist, _ = face_detector.findDistance(face[FACE_LEFT], face[FACE_RIGHT])

                ratio = (eye_dist / face_dist) * 100

                if ratio < 11.0:
                    closed_frames += 1
                else:
                    closed_frames = 0

                if closed_frames >= SLEEP_THRESHOLD_FRAMES:
                    is_sleepy = True

                cvzone.putTextRect(img, f"Eye Ratio: {int(ratio)}", (30, 40), scale=1, thickness=1)
            else:
                closed_frames = 0
                covered_frames += 1
                
                if covered_frames >= COVER_THRESHOLD_FRAMES:
                    is_face_covered = True

            # 2. PHONE DETECTION
            phone_detected = False
            if phone_detector:
                results = phone_detector.predict(img, stream=True, verbose=False)
                for r in results:
                    boxes = r.boxes
                    for box in boxes:
                        cls_id = int(box.cls[0])
                        conf = float(box.conf[0])

                        if classNames.get(cls_id) == "cell phone" and conf > 0.5:
                            phone_detected = True
                            x1, y1, x2, y2 = map(int, box.xyxy[0])
                            cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 2)
                            cvzone.putTextRect(img, f"Phone detected! {int(conf*100)}%", (x1, max(y1 - 10, 30)), scale=1, thickness=1, colorR=(255, 0, 255))

            # 3. ALARM LOGIC & DISPLAY
            if is_face_covered:
                cvzone.putTextRect(img, "DONT COVER YOUR FACE!", (50, 100), scale=2, thickness=3, colorR=(0, 0, 255))
                if not is_audio_busy and alarm_facehide:
                    alarm_facehide.play(0)
                    current_playing = 'facehide'
            elif is_sleepy:
                cvzone.putTextRect(img, "WAKE UP & STUDY!", (50, 100), scale=2, thickness=3, colorR=(0, 0, 255))
                if not is_audio_busy and alarm_sleep:
                    alarm_sleep.play(0)
                    current_playing = 'sleep'
            elif phone_detected:
                cvzone.putTextRect(img, "PUT THE PHONE AWAY!", (50, 100), scale=2, thickness=3, colorR=(0, 165, 255))
                if not is_audio_busy and alarm_phone:
                    alarm_phone.play(0)
                    current_playing = 'phone'
            elif is_audio_busy:
                if current_playing == 'facehide':
                    cvzone.putTextRect(img, "DONT COVER YOUR FACE!", (50, 100), scale=2, thickness=3, colorR=(0, 0, 255))
                elif current_playing == 'sleep':
                    cvzone.putTextRect(img, "WAKE UP & STUDY!", (50, 100), scale=2, thickness=3, colorR=(0, 0, 255))
                elif current_playing == 'phone':
                    cvzone.putTextRect(img, "PUT THE PHONE AWAY!", (50, 100), scale=2, thickness=3, colorR=(0, 165, 255))

            # Convert to QImage for UI
            rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            h, w, ch = rgb_img.shape
            bytes_per_line = ch * w
            qimg = QImage(rgb_img.data, w, h, bytes_per_line, QImage.Format.Format_RGB888)
            
            self.frame_ready.emit(qimg.copy())

        cap.release()
        try:
            if pygame.mixer.get_init():
                pygame.mixer.quit()
        except:
            pass
        self.status_updated.emit("Study Mode Stopped.")

    def stop(self):
        self.running = False
        self.wait()
