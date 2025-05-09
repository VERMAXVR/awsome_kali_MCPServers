import asyncio
from src.kali_mcps.base.kali_command import CommandRunner

class NmapCommand(CommandRunner):
    def __init__(self):
        super().__init__("nmap", 
                        network_enabled=True,  # nmap需要网络访问
                        memory_limit="2g",     # 需要更多内存
                        timeout=300)           # 需要更长的超时时间

def basic_scan_action(target: str) -> tuple[str, str]:
    """
    Basic scan
    For example: nmap 192.168.1.1
    """
    cmd = NmapCommand()
    command = ["nmap", target]
    return cmd.execute(command)

def intense_scan_action(target: str) -> tuple[str, str]:
    """
    Intense scan (-T4 -A)
    Includes: OS detection, version detection, script scanning, and traceroute
    """
    cmd = NmapCommand()
    command = ["nmap", "-T4", "-A", target]
    return cmd.execute(command)

def stealth_scan_action(target: str) -> tuple[str, str]:
    """
    SYN scan (-sS)
    Half-open scan, more stealthy
    Requires root privileges
    """
    cmd = NmapCommand()
    command = ["nmap", "-sS", target]
    return cmd.execute(command)

def quick_scan_action(target: str) -> tuple[str, str]:
    """
    Quick scan (-T4 -F)
    Only scans the most common ports
    """
    cmd = NmapCommand()
    command = ["nmap", "-T4", "-F", target]
    return cmd.execute(command)

def vulnerability_scan_action(target: str) -> tuple[str, str]:
    """
    Vulnerability scan (-sV --script vuln)
    Uses vulnerability detection scripts
    """
    cmd = NmapCommand()
    command = ["nmap", "-sV", "--script", "vuln", target]
    return cmd.execute(command)

if __name__ == "__main__":
    # Test example
    print(quick_scan_action("10.1.1.106"))
