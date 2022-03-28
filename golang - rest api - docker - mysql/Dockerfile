FROM golang:1.17.7-alpine
RUN mkdir -p /src/app
WORKDIR /src/app
COPY . .
#RUN ls

#ENV GOPATH=/src/app

#RUN go mod download
#RUN go run main.go
#EXPOSE 8080
RUN go build -o main .
CMD [ "./main" ]