package com.example.httpserver.mapper;
import com.example.httpserver.entity.firm;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.*;

import java.util.List;

@Mapper
public interface firmMapper {
    List<firm> getFirm();
}
