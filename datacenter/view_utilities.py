def format_duration(duration):
    duration_hours = int(duration // 3600)
    duration_minutes = int((duration % 3600) // 60)
    duration_seconds = int((duration % 3600) % 60)

    formatted_string = '{hours}:{minutes}:{seconds}'.format(
            hours=duration_hours,
            minutes=duration_minutes,
            seconds=duration_seconds,
        )

    return formatted_string
