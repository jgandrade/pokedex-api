import os
import smtplib
from email.message import EmailMessage


class EmailService:
    def __init__(self, smtp_host="smtp.gmail.com", smtp_port=465):
        self.smtp_host = smtp_host
        self.smtp_port = smtp_port
        self.smtp_user = os.getenv("SMTP_EMAIL")
        self.smtp_pass = os.getenv("SMTP_PASSWORD")

    def _send_email(
        self, to_email: str, subject: str, text_content: str, html_content: str
    ):
        msg = EmailMessage()
        msg["From"] = f"ThePokemonProject  <{self.smtp_user}>"
        msg["To"] = to_email
        msg["Subject"] = subject
        msg.set_content(text_content)
        msg.add_alternative(html_content, subtype="html")

        try:
            with smtplib.SMTP_SSL(self.smtp_host, self.smtp_port) as server:
                server.login(self.smtp_user, self.smtp_pass)
                server.send_message(msg)
        except smtplib.SMTPException as e:
            raise smtplib.SMTPException(f"Failed to send email: {str(e)}")

    def send_email_verification(self, email_address: str, name: str, token: str):
        email_verification_url = f"{os.getenv('API_ALLOW_URL', 'http://localhost:5173')}/users/verify?token={token}"

        text_content = f"""
        Welcome to ThePokemonProject  {name}!

        Please verify your email address to activate your account. Click the link below to complete your verification:

        {email_verification_url}

        If you didn't register with ThePokemonProject, please ignore this email.

        Thanks,
        The ThePokemonProject Team
        """

        html_content = f"""
        <div style="font-family: Arial, sans-serif; line-height: 1.6; color: #333;">
          <h2 style="color: #2A9D8F;">Welcome to ThePokemonProject!</h2>
          <p>Thank you for registering with us. Please verify your email address to activate your account.</p>
          <p>
            <a href="{email_verification_url}"
            style="background-color: #2A9D8F; color: white; padding: 10px 20px; text-decoration: none; border-radius: 5px;">
            Verify Email
            </a>
          </p>
          <p>If the button above doesn't work, copy and paste the link below into your web browser:</p>
          <p>{email_verification_url}</p>
          <p>If you didn't register with ThePokemonProject , please ignore this email.</p>
          <br>
          <p>Thanks,<br>The ThePokemonProject Team</p>
        </div>
        """

        self._send_email(
            email_address,
            "Verify Your Email for ThePokemonProject ",
            text_content,
            html_content,
        )
