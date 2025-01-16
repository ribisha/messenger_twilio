# Twilio WhatsApp Messaging Interface
------------------------------------------

This project leverages **Twilio** to send messages directly to WhatsApp contacts and groups without opening the WhatsApp interface. However, certain limitations apply due to account restrictions.

> Features
-----------
    - Send to Individuals: Messages can be sent directly to specific WhatsApp numbers.
    - Send to Groups: Messages can be sent to WhatsApp groups using their invite link.


> Important Notes
------------------
    1. Twilio Sandbox Requirement:
        - Twilio requires recipients to join its **sandbox environment** before they can receive messages.
        - To do this, recipients must send the code `join national-western` to Twilio's WhatsApp number: `+1 415 523 8886`.

    2. Group Messaging:
        - To send a message to a WhatsApp group, use the group’s invite link.
        - Extract the group invite code from the link (e.g., for `https://chat.whatsapp.com/your_group_invite_code`, the code is `your_group_invite_code`) and input it into the provided form.

> Limitations
--------------
    - Messages can only be sent to recipients who have joined the Twilio sandbox environment.
    - Group messaging functionality requires the group invite code to be extracted manually from the invite link.
    - The restrictions exist due to the free-tier limitations of the Twilio account.

> Example Usage
---------------
Individual Messaging
    1. The recipient sends the code `join national-western` to `+1 415 523 8886` to join the Twilio sandbox.
    2. Once joined, use the provided interface to send messages directly.

Group Messaging
----------------
    1. Obtain the WhatsApp group invite link.
    2. Extract the group invite code from the link. For example:

        - Invite Link: `https://chat.whatsapp.com/your_group_invite_code`

        - Invite Code: `your_group_invite_code`

    3. Input the invite code into the interface and send your message.

Additional Information
-----------------------
This project demonstrates Twilio's capabilities for automated WhatsApp messaging. Upgrade to a full Twilio account to remove sandbox restrictions and unlock additional features.

