from email_sender import EmailSender
from services import SendGrid
from test_email_sender import test_email_sender_with_mailchimp


def main() -> None:
    test_email_sender_with_mailchimp()



if __name__ == "__main__":
    main()
