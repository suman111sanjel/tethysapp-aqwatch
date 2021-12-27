import { createApp } from "vue";
import emission from "./views/emission.vue";
import store from "./store/modules/emission";
import ElementPlus from 'element-plus';
import 'element-plus/lib/theme-chalk/index.css';
const app = createApp(emission);
app.use(store);
app.use(ElementPlus);
app.mount('#app');
