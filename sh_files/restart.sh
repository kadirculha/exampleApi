docker rm -f exampleapi

# Remove any existing container named 'exampleapi' forcefully
docker rm -f exampleapi

# Run a new Docker container in the background with the following options:
docker run -d \            # Run the container in detached mode (in the background)
    -ti \                  # Allocate a pseudo-TTY and keep it open even if not attached
    --restart=always \     # Always restart the container unless explicitly stopped
    --name exampleapi \    # Assign the name 'exampleapi' to the container
    -p 8010:8010 \         # Map port 8010 of the host to port 8010 of the container
    exampleapi             # Use the image named 'exampleapi'
