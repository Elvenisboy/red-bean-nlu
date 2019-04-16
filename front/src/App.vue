<template>
  <div id="app">
    <!-- <HelloWorld msg="Welcome to Your Vue.js App"/> -->
    <div class="left-side">
      <div class="left-side-header">
        <span>控制面板</span>
      </div>
      <div class="left-side-content">
        <div class="left-side-content-title">
          <span>slots</span>
          <span class="icon-plus"></span>
        </div>
        <div class="slots">
          <span>你是个傻子呀</span>
          <span>mdzz</span>
          <span>mdzz</span>
          <span>你是个傻子呀</span>
          <span>你是个傻子呀</span>
          <span>你是个傻子呀</span>
          <span>你是个傻子呀</span>
          <span>你是个傻子呀</span>
          <span>你是个傻子呀</span>
          <span>你是个傻子呀</span>
        </div>

        <div class="left-side-content-title">
          <span>intents</span>
          <span class="icon-plus"></span>
        </div>
        <div class="intents">
          <span>你是个傻子呀</span>
          <span>mdzz</span>
          <span>mdzz</span>
          <span>你是个傻子呀</span>
          <span>你是个傻子呀</span>
          <span>你是个傻子呀</span>
          <span>你是个傻子呀</span>
          <span>你是个傻子呀</span>
          <span>你是个傻子呀</span>
          <span>你是个傻子呀</span>
        </div>

        <span>历史记录</span>

        <div class="history-list">
          <ul>
            <li>兔子</li>
            <li>傻兔子</li>
            <li>怎么这么傻</li>
            <li>丢出出去算了 = =</li>
            <li>丢出出去算了 = =</li>
            <li>丢出出去算了 = =</li>
            <li>丢出出去算了 = =</li>
            <li>丢出出去算了 = =</li>
            <li>丢出出去算了 = =</li>
          </ul>
        </div>
      </div>
    </div>
    <div class="center">
      <div class="center-wraper">
        <h3>Slots:</h3>
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
        </div>

        <h3>Text:</h3>
        <div class="text">
          <span class="activate">
            小明
            <small>人物</small>
          </span>
          <span>想</span>
          <span>要</span>
          <span>在</span>
          <span class="activate">
            周末
            <small>人物</small>
          </span>
          <span>和</span>
          <span>朋</span>
          <span>友</span>
          <span>吃</span>
          <span>饭</span>
        </div>

        <h3>Intents:</h3>
        <div class="center-intents">
          <span>1</span>
          <span>你是个二傻子</span>
          <span>你是个二傻子</span>
        </div>

        <div class="actions">
          <span>
            <span class="icon-arrow-left2"></span>
          </span>
          <span>
            <span class="icon-arrow-right2"></span>
          </span>
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
  },
  methods: {
    getMessage() {
      const path = 'http://localhost:8000/api/read_datas/1';
      this.axios.get(path)
        .then((res) => {
          console.log(res.data)
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
  created() {
    // console.log(this)
    this.getMessage();
  },
};
</script>

<style>
@import "~@/assets/style.css";

body {
  padding: 0;
  margin: 0;
  color: #666;
}

#app {
  display: flex;
  flex: 1;
  flex-direction: row;
}

#app .center {
  width: 100%;
  height: 100vh;
}

.center-wraper {
  width: 80%;
  padding-top: 20px;
  padding-left: 10%;
  padding-right: 10%;
}

.center .labels {
  max-height: 25vh;
  display: flex;
  justify-content: space-around;
  align-items: center;
  flex-wrap: wrap;
  overflow-y: scroll;
}

.labels span {
  background: #f5f5f5;
  padding: 15px;
  min-width: 50px;
  margin-right: 15px;
  margin-bottom: 15px;
}

.center .text {
  margin-bottom: 20px;
  font-size: 20px;
  /* height: 20vh; */
}

.center .text .activate {
  background: #363b3e;
  padding: 10px 20px;
  color: #fff;
}

.center .text span:nth-child(1) {
  margin-left: 0;
}

.center .text span {
  margin-left: 10px;
}

.center .text span small {
  font-size: 5px;
}

.center .center-intents {
  max-height: 20vh;
  display: flex;
  justify-content: space-around;
  align-items: center;
  flex-wrap: wrap;
  overflow-y: scroll;
  margin: 20px;
}

.center span {
  background: #f5f5f5;
  padding: 15px;
  min-width: 50px;
  margin-right: 15px;
  margin-bottom: 15px;
}

.center .actions {
  height: 20vh;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.actions span {
  /* margin-top: 20vh; */
  padding: 20px 35px;
  background: #363b3e;
  font-size: 20px;
  color: #fff;
}

#app .left-side {
  width: 25%;
  min-height: 100vh;
  background: #fff;
  box-shadow: 2px 0 10px rgba(0, 0, 0, 0.1);
  z-index: 2;
}

.left-side .left-side-header {
  height: 10vh;
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
  padding: 0 20px;
  display: flex;
  flex-direction: column;
}

.left-side-content .slots,
.intents {
  max-height: 25vh;
  display: flex;
  justify-content: flex-start;
  align-items: center;
  flex-wrap: wrap;
  overflow-y: scroll;
}

.left-side-content .slots span {
  border: 1px solid #363b3e;
  padding: 5px;
  height: 20px;
  margin-right: 5px;
  margin-bottom: 10px;
}

.left-side-content .intents span {
  border: 1px solid #363b3e;
  padding: 5px;
  height: 20px;
  margin-right: 5px;
  margin-bottom: 10px;
}

.left-side-content-title {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.left-side-content .left-side-content-title span {
  margin-top: 10px;
  margin-bottom: 10px;
}

.history-list ul {
  list-style: none;
  margin: 0;
  padding: 0;
  max-height: 20vh;
  overflow-y: scroll;
}

.history-list ul li {
  padding: 5px 0;
}
</style>
