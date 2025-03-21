def generate_invitations(template, attendees):
    """Create personalized files from a template and a list"""

    if not isinstance(template, str):
        print("Error: The template is not a string")
        return

    if not isinstance(attendees, list) or not all(isinstance(attendee, dict) for attendee in attendees):
        print("Error: Attendees is not a list")
        return

    if not template.strip():
        print("Error: The template can't be empty")
        return

    if not attendees:
        print("Error: The attendees list can't be empty")
        return

    for index, attendee in enumerate(attendees, 1):
        processed_template = template
        for key, value in attendee.items():
            placeholder = f"{{{key}}}"
            processed_template = processed_template.replace(
                placeholder, value if value else "N/A")
        output_file = f"output_{index}.txt"
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(processed_template)
