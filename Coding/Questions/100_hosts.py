"""
Write a script that connects to 100 hosts, looks for a particular process and sends an email with a report
"""

import asyncio
import asyncssh
import smtplib
from email.message import EmailMessage

HOSTS = ["host1.example.com", "host2.example.com"]
PROCESS_NAME = "nginx"
EMAIL_TO = "admin@example.com"
EMAIL_FROM = "monitor@example.com"
SMTP_SERVER = "smtp.example.com"

"""
    Async IO lets us run multiple tasks without using miltiple threads or processes. While waiting for I/O, other tasks can execute
    Great for IO bound tasks
"""
async def check_process(host):
    try:
        async with asyncssh.connect(host, username="user") as conn:
            result = await conn.run(f"pgrep -x {PROCESS_NAME}", check=False)
            status = "Running" if result.stdout.strip() else "Not Running"
            return host, status
    except Exception as e:
        return host, f"Error: {e}"

async def gather_reports():
    tasks = [check_process(host) for host in HOSTS]
    results = await asyncio.gather(*tasks)
    return results

def send_email(report):
    msg = EmailMessage()
    msg["Subject"] = f"Process Report for {PROCESS_NAME}"
    msg["From"] = EMAIL_FROM
    msg["To"] = EMAIL_TO
    msg.set_content(report)

    with smtplib.SMTP(SMTP_SERVER) as server:
        server.send_message(msg)

async def main():
    results = await gather_reports()
    report = "\n".join(f"{host}: {status}" for host, status in results)
    send_email(report)
    print("Email sent!")

asyncio.run(main())