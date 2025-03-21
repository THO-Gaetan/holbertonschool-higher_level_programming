def generate_invitations(template, attendees):

    if not isinstance(template, str):
        return("Error: The template is not a string")
    
    if not isinstance(attendees, list):
        return("Error: Attendees is not a list")
    
    if not template.strip():
        return("Error: The template can't be empty")
    
    if not attendees:
        return("Error: The attendees list can't be empty")

    for index, attendee in enumerate(attendees, 1):
        for value in attendee.items():
            placeholder = {"name", "event_title", "event_date", "event_location"}
            processed_template = template.replace(placeholder, value if value else "N/A")
        output_file = f"output_{index}.txt"
        with open(output_file, 'w') as file:
            file.write(processed_template)

