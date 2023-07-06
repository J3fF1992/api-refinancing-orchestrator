FROM 178164760726.dkr.ecr.us-east-1.amazonaws.com/python3.11-base-slim.docker:latest AS base

# LABELS
LABEL maintainer="Lendico <contato@lendico.com.br>"
LABEL slack="squad-credit"
LABEL application="api-refinancing-orchestrator"
LABEL repository="git@bitbucket.org:lendicobrasil/api-refinancing-orchestrator.git"

# Copy project main folder
COPY aro aro

# Testing stage
FROM base AS testing

# Install testing packages (customize according to this application)
# Note: Do not put any lib here except for testing.
#       These libs will only be installed in the test container
RUN pip install coverage freezegun mock pytest pytest-cov pytest-mock requests-mock mixer moto --no-cache-dir

# Run tests
COPY tests tests
RUN coverage run -m pytest -vvs --junitxml=/report.xml
RUN coverage xml -o /coverage.xml -i

# Final stage
FROM base AS final

COPY --from=testing /coverage.xml /
COPY --from=testing /report.xml /

RUN mkdir -p aro

## insert custom codes from application here

EXPOSE 5000
ENTRYPOINT ["./entrypoint.sh"]
