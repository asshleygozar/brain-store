# BUILDER
FROM python:3.12-slim AS builder
WORKDIR /app

# Update and install gcc compiler to ensure that required python packages libraries and drivers will work properly
RUN apt-get update && apt-get install -y --no-install-recommends gcc
RUN pip install uv 

# UV LINK for copying files rather than using Hardlink
# UV COMPILE for pre compiling into bytecode for optimization
# UV PYTHON DOWNLOADS to prevent downloading own python versions
ENV UV_LINK_MODE=copy \
    UV_COMPILE_BYTECODE=1 \
    UV_PYTHON_DOWNLOADS=never

# For caching the downloading of dependencies
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-install-project

# Then copy the whole application code
COPY . .

# Install project into venv with copied code
RUN uv sync --frozen

# FINAL BUILDER
FROM python:3.12-slim AS runner
WORKDIR /app

# COPY application code to my directory /app and /.venv
COPY --from=builder /app/app /app/app
COPY --from=builder /app/.venv /app/.venv

# To use the virtual executables when running python or uvicorn
ENV PATH="/app/.venv/bin:$PATH"

# Default PORT
ENV PORT=8080

CMD [ "sh","-c","uvicorn app.main:app --host 0.0.0.0 --port ${PORT}" ]