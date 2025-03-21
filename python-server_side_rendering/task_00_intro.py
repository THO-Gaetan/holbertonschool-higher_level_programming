def generate_invitations(template, attendees):
    """Create personalized files from a template and a list"""

    if not isinstance(template, str):
        return ("Error: The template is not a string")

    if not isinstance(attendees, list) or not all(isinstance(attendee, dict) for attendee in attendees):
        return ("Error: Attendees is not a list")

    if not template.strip():
        return ("Error: The template can't be empty")

    if not attendees:
        return ("Error: The attendees list can't be empty")

    for index, attendee in enumerate(attendees, 1):
        processed_template = template
        for key, value in attendee.items():
            placeholder = f"{{{key}}}"
            processed_template = processed_template.replace(
                placeholder, value if value else "N/A")
        output_file = f"output_{index}.txt"
        with open(output_file, 'w') as file:
            file.write(processed_template)
