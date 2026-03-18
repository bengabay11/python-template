ARG PYTHON_VERSION=3.10
FROM python:${PYTHON_VERSION}-slim

ENV PYTHONUNBUFFERED=1

RUN pip install --no-cache-dir uv==0.10.11

RUN useradd -m -u 1000 appuser

RUN mkdir -p /app && chown appuser:appuser /app
WORKDIR /app

# Copy dependency files first for better layer caching
COPY --chown=appuser:appuser pyproject.toml ./

# Install project dependencies (from pyproject.toml)
RUN uv pip install --system --no-cache .

# Copy application code
COPY --chown=appuser:appuser src/ src/
COPY --chown=appuser:appuser config/ config/

USER appuser

ENTRYPOINT ["python", "-m", "src.main"]
