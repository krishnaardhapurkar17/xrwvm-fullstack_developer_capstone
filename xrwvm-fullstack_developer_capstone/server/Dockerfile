FROM python:3.12.0-slim-bookworm

ENV PYTHONUNBUFFERED 1
ENV PYTHONWRITEBYTECODE 1

ENV APP=/app

# Change the workdir.
WORKDIR $APP

# Install the requirements
COPY requirements.txt $APP

RUN pip3 install -r requirements.txt

# Copy the rest of the files
COPY . $APP

EXPOSE 8000

# Make the entrypoint script executable
RUN chmod +x /app/entrypoint.sh

# Specify the entrypoint script
ENTRYPOINT ["/bin/bash","/app/entrypoint.sh"]

# The default command to run after the entrypoint
CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "djangoproj.wsgi"]