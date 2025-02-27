package com.example.httpserver.controller;

import com.example.httpserver.service.firmService;
import lombok.Data;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;
import com.example.httpserver.entity.firm;

import java.util.List;

@RestController
@CrossOrigin(origins = "http://localhost:8080") // 允许来自 http://localhost:8080 的请求
public class firmController {

    @Autowired
    private firmService fService;//controller只需调用服务和确定路径，跟实体和其他的无关了

    @GetMapping("/firm")
    public List<firm> login() {
        if (fService.getgetfirm()!=null) {
            return fService.getgetfirm();
        } else {
            return null;
        }
    }
    @Data
    public static class user{
        String username;
        String password;
    }
}
