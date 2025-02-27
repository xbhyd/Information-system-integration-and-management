package com.example.httpserver.service;
import com.example.httpserver.entity.firm;
import com.example.httpserver.mapper.firmMapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import java.util.List;

@Service
public class firmService {
    @Autowired
    private firmMapper fMapper;
    public List<firm> getgetfirm() {//从Mapper获取数据并定义验证用户名和密码的API，该函数传入的参数均来自前端
        return fMapper.getFirm();
    }
}