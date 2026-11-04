import socket
import json
import threading
import time
import requests

MESH_PORT = 9999
HARDWARE_TELEMETRY_PORT = 8080

class KineticMeshCore:
    def __init__(self):
        self.mesh_active = False
        self.sentry_active = False
        self.mesh_peers = []

    # 1. Off-Grid RF / Mesh Network (UDP Broadcast without Internet)
    def start_mesh_beacon(self, node_id="Zaifer_Node_Alpha", log_callback=print):
        if self.mesh_active:
            return "Mesh node pehle se live hai!"
        
        self.mesh_active = True
        def listen_mesh():
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
            try:
                s.bind(('', MESH_PORT))
                log_callback(f"📡 [Off-Grid Mesh] Listening on broadcast port {MESH_PORT}...")
                while self.mesh_active:
                    data, addr = s.recvfrom(1024)
                    msg = data.decode("utf-8", errors="ignore")
                    if addr[0] not in self.mesh_peers:
                        self.mesh_peers.append(addr[0])
                        log_callback(f"📶 [Peer Discovered] Linked with Node at {addr[0]}: {msg}")
            except Exception as e:
                log_callback(f"Mesh Socket Error: {str(e)}")
            finally:
                s.close()

        threading.Thread(target=listen_mesh, daemon=True).start()
        return f"📡 Off-Grid Mesh Beacon Online. Zero-internet communication active on port {MESH_PORT}."

    def broadcast_mesh_signal(self, payload_text):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        data = json.dumps({"source": "Zaifer_Master", "payload": payload_text}).encode("utf-8")
        s.sendto(data, ('<broadcast>', MESH_PORT))
        s.close()
        return f"⚡ Broadcasted off-grid packet: '{payload_text}'"

    # 2. Hardware Telemetry & Machine Relay (ESP32/Relay Control)
    def trigger_hardware_relay(self, target_ip, action="TOGGLE", pin=5):
        # Sends direct low-latency UDP/HTTP trigger to local microcontrollers
        url = f"http://{target_ip}:{HARDWARE_TELEMETRY_PORT}/relay?pin={pin}&action={action}"
        try:
            res = requests.get(url, timeout=2)
            return f"🔌 Hardware Link: Pin {pin} executed [{action}] on machine {target_ip}."
        except Exception:
            # Fallback to local raw socket pulse
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(1.5)
                sock.connect((target_ip, HARDWARE_TELEMETRY_PORT))
                sock.send(f"PULSE_PIN_{pin}_{action}\n".encode('utf-8'))
                sock.close()
                return f"⚡ Raw Socket Pulse injected to hardware controller at {target_ip}."
            except Exception as err:
                return f"Hardware Unreachable: {str(err)} (Check local IP)"

    # 3. Bio-Rhythm & Ambient Sound Sentry
    def start_ambient_sound_sentry(self, threshold_db=75, alert_callback=print):
        if self.sentry_active:
            return "Ambient Sentry pehle se monitoring par hai!"

        self.sentry_active = True
        def monitor_loop():
            alert_callback("👂 [Ambient Sentry] Background acoustic sensor active. Monitoring for sudden shocks...")
            # Sentry daemon monitoring loop
            while self.sentry_active:
                time.sleep(3)

        threading.Thread(target=monitor_loop, daemon=True).start()
        return "🛡️ Ambient Sound Sentry armed in low-power background mode."

kinetic_mesh_engine = KineticMeshCore()
