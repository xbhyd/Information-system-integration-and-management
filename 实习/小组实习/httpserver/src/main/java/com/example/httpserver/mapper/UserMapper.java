package com.example.httpserver.mapper;
import com.example.httpserver.entity.user;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.*;

@Mapper
public interface UserMapper {
    user findByUsername(String username);
}