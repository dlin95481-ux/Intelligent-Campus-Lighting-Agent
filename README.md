# Intelligent Campus Lighting Management Agent

## 项目简介
本项目是一个基于 AI Agent 架构的智慧校园照明管理中枢。它通过长链条逻辑推理（Long-chain Reasoning），实现了对校园照明设备的精细化能效控制，解决了传统感应灯“误触发”和“调节生硬”的痛点。

## 技术栈
- **核心算法**: 自适应调光逻辑 (Self-adaptive Dimming)
- **通信协议**: ZigBee (硬件侧), MQTT (控制侧)
- **硬件环境**: STM32 主控, INA226 功耗监测, ESP8266 联网模块
- **开发语言**: Python (Agent 端), C (嵌入式端)

## AI Agent 逻辑流
1. **Perception**: 异步采集多维度传感器数据。
2. **Reasoning**: 结合当前环境光、历史能耗曲线及人员轨迹进行多级逻辑判定。
3. **Action**: 动态计算 PWM 占空比，并通过 MQTT 实时同步至硬件执行端。

## 性能指标
- **节能率**: 相比传统方案提升约 35%。
- **响应时延**: 控制链路延迟 < 100ms。
