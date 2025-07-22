
def generate_invitations(template, attendees):
    
    inv_num = 0
    if not isinstance(template, str):
        raise TypeError("Template must be a string")
    if template.strip() == "":
        raise ValueError("Template is empty")
    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        raise TypeError("Attendees must be a list of dictionaries")

    for attendee in attendees:
        
        invitation = template.format(
            name=attendee.get("name", "N/A"),
            event_title=attendee.get("event_title", "N/A"),
            event_date=attendee.get("event_date", "N/A"),
            event_location=attendee.get("event_location", "N/A")
        )
        inv_num += 1
        with open(f"output_{inv_num}.txt", "w") as f:
            f.write(invitation)

        print(invitation)
