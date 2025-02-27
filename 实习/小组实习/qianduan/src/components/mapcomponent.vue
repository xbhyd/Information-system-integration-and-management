<script setup>
import axios from 'axios';
import { onMounted, ref, onUnmounted } from "vue";
import AMapLoader from "@amap/amap-jsapi-loader";

let mapm;
mapm =ref(null);
const errorMessage = ref('');

onMounted(() => {
  window._AMapSecurityConfig = {
    securityJsCode: "a238be446576aeef94aa3a1eea0625c8",
  };
  AMapLoader.load({
    key: "8398c9387101f33340362e421235a3c6", // 申请好的Web端开发者Key，首次调用 load 时必填
    version: "2.0", // 指定要加载的 JSAPI 的版本，缺省时默认为 1.4.15
    plugins: ["AMap.Scale",'AMap.Text'], //需要使用的的插件列表，如比例尺'AMap.Scale'，支持添加多个如：['...','...']
  })
      .then((AMap) => {
        mapm.value = new AMap.Map("container", {
          // 设置地图容器id
          viewMode: "3D", // 是否为3D地图模式
          zoom: 11, // 初始化地图级别
          center: [114.3567, 30.5787], // 初始化地图中心点位置
        });

  axios.get('http://localhost:2020/firm')
      .then(response => {
          console.log('Raw response:', response);
          console.log('Type of response.data:', typeof response.data);
            const firms = response.data.map(firm => ({
              name: firm.firmname, // 使用 firmname 代替 name
              longitude: firm.longitude,
              latitude: firm.latitude
            }));

            console.log('Fetched and processed firms:', firms);

            firms.forEach(firm => {
              var text = new AMap.Text({
                style: {
                  padding: ".5rem .75rem", // 减小内边距
                  "margin-bottom": ".5rem", // 减小底部外边距
                  "border-radius": ".2rem", // 减小圆角半径
                  "background-color": "white",
                  width: "10rem", // 减小宽度
                  "box-shadow": "0 1px 4px 0 rgba(114, 124, 245, .5)", // 减小阴影效果
                  "text-align": "center",
                  "font-size": "16px", // 减小字体大小
                  color: "black",
                },
                position: [firm.longitude, firm.latitude],
                text: firm.name,
              });
              text.setMap(mapm.value); // 注意这里使用的是 map.value
            });
      }).catch(err => {
        console.error('Error fetching data or adding markers:', err);
        errorMessage.value = err.message || 'Failed to fetch data or add markers';
      });
      }).catch((e) => {
      console.log(e);
    });
});



onUnmounted(() => {
  if(this.map){
    mapm.destroyed();
  }
});
</script>

<template>
  <div id="container"></div>
</template>

<style scoped>
#container {
  width: 100%;
  height: 800px;
}
</style>


