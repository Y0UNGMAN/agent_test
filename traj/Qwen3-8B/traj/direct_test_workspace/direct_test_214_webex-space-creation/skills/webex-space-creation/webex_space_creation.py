import sys, json

if __name__ == '__main__':
    args = sys.argv[1:]
    if not args:
        print(json.dumps({"status": "error", "message": "Missing arguments"}))
        sys.exit(1)

    space_name = None
    members = []
    i = 0
    while i < len(args):
        if args[i].lower() == "--name":
            space_name = args[i+1]
            i += 2
        elif args[i].lower() == "--members":
            members = args[i+1].split(',') if i+1 < len(args) else []
            i += 2
        else:
            i += 1

    if not space_name:
        print(json.dumps({"status": "error", "message": "Missing space name"}))
        sys.exit(1)

    print(json.dumps({
        "status": "success",
        "message": f"Webex Space '{space_name}' created successfully.",
        "members": members or ["creator@example.com"]
    }))