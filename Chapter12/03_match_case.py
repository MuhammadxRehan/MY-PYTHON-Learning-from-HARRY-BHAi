def http_status(status):
    match status:
        case 200:
            return "Its ok"
        case 404:
            return "Not Found"
        case 500:
            return "ready to run"
        case 550:
            return "system reload"
        case _:
            return "Out of Syllabus"
print(http_status(00))
        