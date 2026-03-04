FROM nginx:alpine

# Remove default nginx page
RUN rm -rf /usr/share/nginx/html/*

# Copy our custom HTML
COPY index.html /usr/share/nginx/html/index.html
