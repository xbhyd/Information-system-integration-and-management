package com.example.httpserver.controller;

import com.example.httpserver.service.UserService;
import lombok.Data;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

@RestController
@CrossOrigin(origins = "http://localhost:8080") // 允许来自 http://localhost:8080 的请求
public class UserController {

    @Autowired
    private UserService userService;//controller只需调用服务和确定路径，跟实体和其他的无关了

    @PostMapping("/login")
    public boolean login(@RequestBody user user) {
        if (userService.validateLogin(user.username, user.password)) {
            return true;
        } else {
            return false;
        }
    }
    @Data
    public static class user{
        String username;
        String password;
    }
}