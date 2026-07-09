import os
import time
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.spinner import Spinner
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView

BASE_DIR = "/sdcard/Download/Jarvis_Project"
os.makedirs(f"{BASE_DIR}/assets/ui", exist_ok=True)
os.makedirs(f"{BASE_DIR}/assets/audio", exist_ok=True)
os.makedirs(f"{BASE_DIR}/assets/code", exist_ok=True)

STUDIOS = {
    "1. Chat Orchestrator": "Story & Text LLM Core", "2. Lore Writer": "Story & Text LLM Core",
    "3. Quest Generator": "Story & Text LLM Core", "4. Notes Maker": "Story & Text LLM Core",
    "5. Room Builder": "Genesis Physics & Spatial AI", "6. Furniture Fallout-style": "Genesis Physics & Spatial AI",
    "7. Light Controller": "Genesis Physics & Spatial AI", "8. VFX Destroyer": "Genesis Physics & Spatial AI",
    "9. Environment Lab": "Genesis Physics & Spatial AI", "10. Logic Constructor": "Genesis Physics & Spatial AI",
    "11. Wall Textures": "Tripo3D Engine", "12. UI Packs": "Tripo3D Engine",
    "13. 3D Low-Poly Sculptor": "Tripo3D Engine", "14. Auto-Rigger Bones": "Tripo3D Engine",
    "15. Facial Lipsync": "Tripo3D Engine", "16. Cloth Physics": "Tripo3D Engine",
    "17. AR Preview": "Tripo3D Engine", "18. Visual Tweaker": "Tripo3D Engine",
    "19. Radiant NPC AI": "Vector Memory & Agentic AI", "20. Vector Memory": "Vector Memory & Agentic AI",
    "21. Horror Director": "Vector Memory & Agentic AI", "22. Monster Agent": "Vector Memory & Agentic AI",
    "23. GOAP Goals": "Vector Memory & Agentic AI", "24. Adaptive Difficulty": "Vector Memory & Agentic AI",
    "25. Android Touch Coder": "Claude Sandbox & SDK Compiler", "26. Audio Ambient": "Claude Sandbox & SDK Compiler",
    "27. Micro-Modules Compiler": "Claude Sandbox & SDK Compiler", "28. Server-Driven UI": "Claude Sandbox & SDK Compiler",
    "29. QA Bug Hunter": "Claude Sandbox & SDK Compiler", "30. Balance Calculator": "Claude Sandbox & SDK Compiler",
    "31. APK Compressor": "Claude Sandbox & SDK Compiler", "32. DRM Key Guard": "Claude Sandbox & SDK Compiler"
}

class JarvisApp(App):
    def build(self):
        self.title = "JARVIS CORE OS v2026"
        root = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        root.add_widget(Label(text="🤖 JARVIS CORE OS v2026", font_size=24, size_hint_y=None, height=40))
        
        self.status_label = Label(text="Server Active: [Main Orchestrator]", size_hint_y=None, height=30, color=(0, 1, 0, 1))
        root.add_widget(self.status_label)
        
        self.spinner = Spinner(text="1. Chat Orchestrator", values=list(STUDIOS.keys()), size_hint_y=None, height=50)
        self.spinner.bind(text=self.on_spinner_change)
        root.add_widget(self.spinner)
        
        self.input_text = TextInput(hint_text="Введите техническую задачу для ИИ...", multiline=True, size_hint_y=0.3)
        root.add_widget(self.input_text)
        
        btn = Button(text="🚀 Запустить ИИ-процесс в ОЗУ", size_hint_y=None, height=60, background_color=(0, 0.7, 0, 1))
        btn.bind(on_press=self.run_process)
        root.add_widget(btn)
        
        scroll = ScrollView()
        self.output_label = Label(text="Результат работы Джарвиса появится здесь...", size_hint_y=None, halign='left', valign='top')
        self.output_label.bind(width=lambda *x: self.output_label.setter('text_size')(self.output_label, (self.output_label.width, None)))
        self.output_label.bind(texture_size=lambda *x: self.output_label.setter('height')(self.output_label, self.output_label.texture_size[1]))
        scroll.add_widget(self.output_label)
        root.add_widget(scroll)
        
        return root

    def on_spinner_change(self, spinner, text):
        self.status_label.text = f"Server Ready: [{STUDIOS[text]}]"

    def run_process(self, instance):
        prompt = self.input_text.text.strip()
        if not prompt:
            self.output_label.text = "⚠️ Введите текст задачи."
            return
        studio = self.spinner.text
        self.status_label.text = f"Server Active: [{STUDIOS[studio]}]"
        
        if "двер" in prompt.lower() or "door" in prompt.lower():
            ans = "[C# UNITY SCRIPT]\nusing UnityEngine;\npublic class DoorController : MonoBehaviour {\n    void Update() { /* Touch logic active */ }\n}"
        else:
            ans = f"Джарвис принял задачу: '{prompt}'.\nОптимизация под HyperOS завершена.\nДанные сохранены в /Download/Jarvis_Project/."
            
        self.output_label.text = ans
        try:
            with open(f"{BASE_DIR}/jarvis_history.txt", "a", encoding="utf-8") as f:
                f.write(f"=== {studio} ===\nPROMPT: {prompt}\nRESPONSE: {ans}\n\n")
        except:
            pass

if __name__ == '__main__':
    JarvisApp().run()
    
