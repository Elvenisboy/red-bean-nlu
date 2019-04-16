<template>
  <div id="app">
    <!-- <HelloWorld msg="Welcome to Your Vue.js App"/> -->
    <div class="left-side">
      <div class="left-side-header">
        <span>控制面板</span>
      </div>
      <div class="left-side-content">
        <span>历史记录</span>

        <div class="history-list">
          <ul>
            <li>兔子</li>
            <li>傻兔子</li>
            <li>怎么这么傻</li>
            <li>丢出出去算了 = =</li>
          </ul>
        </div>
      </div>
    </div>
    <div class="center">
      <div class="center-wraper">
        <div class="labels">
          <span>1</span>
          <span>你是个二傻子</span>
          <span>你是个二傻子</span>
          <span>你是个二傻子</span>
          <span>你是个二傻子</span>
          <span>你是个二傻子</span>
          <span>你是个二傻子</span>
          <span>你是个二傻子</span>
          <span>你是个二傻子</span>
          <span>你是个二傻子</span>
          <span>你是个二傻子</span>
          <span>你是个二傻子</span>
          <span>你是个二傻子</span>
          <span>你是个二傻子</span>
          <span>你是个二傻子</span>
          <span>你是个二傻子</span>
          <span>你是个二傻子</span>
          <span>你是个二傻子</span>
          <span>你是个二傻子</span>
          <span>你是个二傻子</span>
          <span>你是个二傻子</span>
          <span>你是个二傻子</span>
          <span>你是个二傻子</span>
          <span>你是个二傻子</span>
          <span>你是个二傻子</span>
          <span>你是个二傻子</span>
          <span>你是个二傻子</span>
          <span>你是个二傻子</span>
          <span>你是个二傻子</span>
          <span>你是个二傻子</span>
          <span>你是个二傻子</span>
          <span>你是个二傻子</span>
          <span>你是个二傻子</span>
          <span>你是个二傻子</span>
          <span>你是个二傻子</span>
          <span>你是个二傻子</span>
          <span>你是个二傻子</span>
          <span>你是个二傻子</span>
          <span>你是个二傻子</span>
          <span>你是个二傻子</span>
          <span>你是个二傻子</span>
          <span>你是个二傻子</span>
          <span>你是个二傻子</span>
          <span>你是个二傻子</span>
          <span>你是个二傻子</span>
          <span>你是个二傻子</span>
          <span>你是个二傻子</span>
          <span>你是个二傻子</span>
          <span>你是个二傻子</span>
          <span>你是个二傻子</span>
          <span>你是个二傻子</span>
          <span>你是个二傻子</span>
          <span>你是个二傻子</span>
          <span>你是个二傻子</span>
          <span>你是个二傻子</span>
        </div>
        <div class="text">
          <span>小</span>
          <span>明</span>
          <span>想</span>
          <span>要</span>
          <span>在</span>
          <span>周</span>
          <span>末</span>
          <span>和</span>
          <span>朋</span>
          <span>友</span>
          <span>吃</span>
          <span>饭</span>
        </div>

        <div class="actions">
          <span>-></span>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
// import HelloWorld from './components/HelloWorld.vue'

export default {
  name: "app",
  components: {
    // HelloWorld
  }
};
</script>

<style>
body {
  padding: 0;
  margin: 0;
}

#app {
  display: flex;
  flex: 1;
  flex-direction: row;
  /* justify-content: space-around; */
  /* align-items: center */
}

#app .center {
  width: 100%;
  /* padding: 20px; */
  height: 100vh;
}

.center-wraper {
  width: 80%;
  padding-top: 20px;
  padding-left: 10%;
  padding-right: 10%;
}

.center .labels {
  max-height: 30vh;
  /* margin-bottom: 10px; */
  display: flex;
  justify-content: flex-start;
  align-items: center;
  flex-wrap: wrap;
  overflow-y: scroll;
}

.labels span {
  background: blue;
  padding: 15px;
  min-width: 50px;
  margin-right: 15px;
  margin-bottom: 15px;
}

.center .text {
  margin-top: 20px;
  font-size: 20px;
  height: 40vh;
}

.center .text span:nth-child(1) {
  margin-left: 0;
}

.center .text span {
  margin-left: 10px;
}

.center .actions {
  height:20vh;
  /* background: blue; */
  display: flex;
  justify-content: center;
  align-items: center;
}

.actions span {
  padding:20px 25px;
  background: greenyellow;
  font-size: 20px;
}

#app .left-side {
  width: 25%;
  height: 100vh;
  background: #fff;
  box-shadow: 2px 0 10px rgba(0, 0, 0, 0.1);
  z-index: 2;
}

.left-side .left-side-header {
  height: 60px;
  text-align: center;
  width: 100%;
  display: flex;
  flex: 1;
  flex-direction: row;
  align-items: center;
  justify-content: center;
}

.left-side-header span {
  font-size: 20px;
  font-weight: 600;
}

.left-side-content {
  text-align: left;
  padding: 20px;
}

.history-list ul {
  list-style: none;
  margin: 0;
  padding: 0;
}

.history-list ul li:nth-child(1) {
  padding-top: 20px;
}

.history-list ul li {
  /* list-style-type: none; */
  padding: 5px 0;
}
</style>
