from base64 import b64decode
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
import json

from pytdv2.device import Device, Meta


def get_private_key(base64_private_key):
    try:
        # private_key_data = b64decode(base64_private_key)
        private_key = RSA.import_key(base64_private_key)
        return private_key
    except Exception as e:
        raise Exception("Error generating private key") from e


class Utils:
    def __init__(self, private_key):
        self.private_key = private_key

    def decrypt_response(self, encrypted_meta):
        try:
            encrypted_bytes = b64decode(encrypted_meta)
            private_key = get_private_key(self.private_key)
            cipher = PKCS1_v1_5.new(private_key)
            decrypted_bytes = cipher.decrypt(encrypted_bytes, Meta)
            json_str = decrypted_bytes.decode("utf-8")
            # Langkah 2: Ubah string JSON menjadi dictionary
            data = json.loads(json_str)

            # Langkah 3: Buat objek Meta dari dictionary
            device = Device(**data["device_id"])
            meta_obj = Meta(
                fazpass_id=data.get("fazpass_id", None),
                scoring=data.get("scoring", None),
                risk_level=data.get("risk_level", None),
                is_active=data.get("is_active",None),
                time_stamp=data.get("time_stamp",None),
                platform=data.get("platform",None),
                is_rooted=data.get("is_rooted",None),
                is_emulator=data.get("is_emulator",None),
                is_gps_spoof=data.get("is_gps_spoof",None),
                is_app_tempering=data.get("is_app_tempering",None),
                is_vpn=data.get("is_vpn",None),
                is_clone_app=data.get("is_clone_app",None),
                is_screen_sharing=data.get("is_screen_sharing",None),
                is_debug=data.get("is_debug",None),
                application=data.get("application",None),
                device_id=device,
                sim_serial=data.get("sim_serial",None),
                sim_operator=data.get("sim_operator",None),
                geolocation=data.get("geolocation",None),
                client_ip=data.get("client_ip",None),
                is_notifiable=data.get("is_notifiable", None),
                notifiable_devices= data.get("notifiable_devices", None)
            )
            return meta_obj
        except Exception as e:
            print(f"Error: {e}")
            return None
