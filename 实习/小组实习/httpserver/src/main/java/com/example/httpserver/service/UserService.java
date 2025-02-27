package com.example.httpserver.service;
import com.example.httpserver.entity.user;
import com.example.httpserver.mapper.UserMapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class UserService {

    @Autowired
    private UserMapper userMapper;

    public boolean validateLogin(String username, String password) {//从Mapper获取数据并定义验证用户名和密码的API，该函数传入的参数均来自前端
        user user = userMapper.findByUsername(username);
        return user != null && user.getPassword().equals(password);
    }
}