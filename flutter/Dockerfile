# Use an image with both Python and Flutter
FROM python:3.13.0a4-bookworm

# Install Flutter dependencies (assuming Flutter SDK is used in your project)
# ...

# Create and set the working directory
RUN mkdir /app/
COPY . /app/
WORKDIR /app/

# Expose the port
EXPOSE 9000

# Make server startup script executable
RUN chmod +x server.sh

# Set the entry point to start the web server
ENTRYPOINT ["./server.sh"]