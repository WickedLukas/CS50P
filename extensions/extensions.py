# Ask user.
file_name = input("File name: ").strip().lower()

# Get the file extension without the period.
file_name_split = file_name.rsplit(".", 1)
extension = ""
if len(file_name_split) > 1:
    extension = file_name_split[-1]

# Get media type
media_type = ""
match extension:
    case "gif" | "jpeg" | "png":
        media_type = "image/" + extension
    case "jpg":
        media_type = "image/jpeg"
    case "pdf" | "zip":
        media_type = "application/" + extension
    case "txt":
        media_type = "text/plain"
    case _:
        media_type = "application/octet-stream"

# Respond to user.
print(media_type)
