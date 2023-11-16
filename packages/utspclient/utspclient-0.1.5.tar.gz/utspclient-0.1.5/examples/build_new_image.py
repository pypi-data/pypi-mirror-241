"""
This example shows how to send a tar file containing the build context for a docker image
to the server, so that the server builds the new provider image.
This is done because the build context is usually significantly smaller than 
the built docker image file.
"""

import requests


def main():
    URL = "http://134.94.131.167:443/api/v1/buildimage"
    API_KEY = "OrjpZY93BcNWw8lKaMp0BEchbCc"

    file_path = r"examples\HiSim.tar.gz"
    files = {"hisim-1.0.0.1": open(file_path, "rb")}
    assert (
        next(iter(files)).count("-") == 1
    ), "Invalid provider name: must contain exactly one dash"

    reply = requests.post(URL, files=files, headers={"Authorization": API_KEY})
    print(reply.text)


if __name__ == "__main__":
    main()
