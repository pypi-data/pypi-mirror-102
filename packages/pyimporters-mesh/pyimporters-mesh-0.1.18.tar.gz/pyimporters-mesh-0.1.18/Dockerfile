FROM python:3.8-alpine

# Process update/upgrade
RUN apk update && apk upgrade

# Install prerequisites libxslt-dev, g++, gcc
RUN apk add --update --no-cache g++ gcc libxslt-dev

# Install git
RUN apk add --no-cache git

# Enable Installing packages as root
ENV FLIT_ROOT_INSTALL=1

# Add pyproject.toml + README.md for flit install
ADD pyproject.toml pyproject.toml
ADD README.md README.md
