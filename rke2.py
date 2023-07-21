import subprocess

def run_command(command):
    try:
        subprocess.run(command, shell=True, check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Command execution failed with error: {e}")
        return False

if __name__ == "__main__":
    print("Running RKE2 installation script...")
    if run_command("curl -sfL https://get.rke2.io | sh -"):
        print("RKE2 installed successfully.")
        print("Enabling and starting RKE2 service...")
        if run_command("systemctl enable rke2-server.service") and run_command("systemctl start rke2-server.service"):
            print("RKE2 service enabled and started.")
            print("Showing journal logs for RKE2 server...")
            run_command("journalctl -u rke2-server -f")
        else:
            print("Failed to enable and start RKE2 service.")
    else:
        print("RKE2 installation failed.")
