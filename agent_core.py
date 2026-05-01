import json
import time

class LightingAgent:
    """
    智能校园照明 Agent (Intelligent Campus Lighting Agent)
    核心逻辑：感知 -> 推理 -> 决策 -> 执行
    """
    def __init__(self):
        self.energy_threshold = 0.8  # 能效阈值
        self.current_mode = "ECO"    # 默认节能模式

    def perception_layer(self, sensor_data):
        """
        感知层：接收来自 ZigBee 网络的传感器数据
        """
        light_intensity = sensor_data.get("lux", 0)
        human_presence = sensor_data.get("motion", False)
        print(f"[感知] 当前环境光照: {light_intensity}lx, 人员活动: {human_presence}")
        return light_intensity, human_presence

    def reasoning_chain(self, lux, motion):
        """
        长链条推理：判断当前是否需要调光
        逻辑：不仅看实时数值，还要推理“必要性”
        """
        decision_log = []
        
        # 第一层推理：自然光是否充足？
        if lux > 300:
            decision_log.append("自然光充足，无需人工光源补偿。")
            target_brightness = 0
        else:
            # 第二层推理：是否有人员活动？
            if motion:
                decision_log.append("光照不足且有人员活动，需要高亮度照明。")
                target_brightness = 100
            else:
                decision_log.append("光照不足但无人员活动，切换至低功耗维持模式。")
                target_brightness = 10
        
        print(f"[推理链条] { ' -> '.join(decision_log) }")
        return target_brightness

    def execution_layer(self, brightness):
        """
        执行层：通过 MQTT 下发指令给 STM32 控制器
        """
        payload = {
            "device": "campus_lamp_01",
            "cmd": "SET_PWM",
            "value": brightness,
            "timestamp": time.time()
        }
        # 模拟下发 MQTT 消息
        print(f"[执行] 下发控制指令至硬件: {json.dumps(payload)}")
        return True

    def run_agent_loop(self, mock_data):
        """
        Agent 运行主循环
        """
        print("--- Agent 推理周期开始 ---")
        lux, motion = self.perception_layer(mock_data)
        target = self.reasoning_chain(lux, motion)
        self.execution_layer(target)
        print("--- Agent 推理周期结束 ---\n")

# 模拟测试数据
if __name__ == "__main__":
    agent = LightingAgent()
    
    # 场景 1: 白天，没人
    agent.run_agent_loop({"lux": 450, "motion": False})
    
    # 场景 2: 晚上，有人
    agent.run_agent_loop({"lux": 50, "motion": True})
