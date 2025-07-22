
def generate_invitations(template, attendees):
    for attendee in attendees:
        if not isinstance(template, str):
            raise TypeError("Template must be a string")
        
        invitation = template.format(
            name=attendee.get("name", "N/A"),
            event_title=attendee.get("event_title", "N/A"),
            event_date=attendee.get("event_date", "N/A"),
            event_location=attendee.get("event_location", "N/A")
        )

        print(invitation)
