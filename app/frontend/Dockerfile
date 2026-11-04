## STAGE 1: Build the React app WITH Node.js
FROM node:20-alpine AS builder

WORKDIR /app

COPY package.json package-lock.json ./
RUN npm ci --ignore-scripts

COPY index.html ./
COPY src ./src

RUN npm run build

# STAGE 2: Serve compiled HTML/JS with lightweight Nginx

FROM nginxinc/nginx-unprivileged:alpine-slim

USER root
RUN apk add --no-cache 'pcre2>=10.49-r0'
USER 101:101

COPY --from=builder /app/dist /usr/share/nginx/html

EXPOSE 8080

## entrypoint for the frontend service

CMD ["nginx", "-g", "daemon off;"]
