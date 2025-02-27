package com.example.httpserver;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.io.File;


@SpringBootApplication
public class HttpserverApplication {

    public static void main(String[] args) {
        SpringApplication.run(HttpserverApplication.class, args);
    }

}
