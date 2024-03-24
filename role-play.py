import json

# 假设我们有一个简单的函数来生成角色人设
def generate_character_profile(text):
    # 这里只是一个示例，实际应用中可能需要使用更复杂的 NLP 模型
    return {"name": "角色名", "description": "基于文本生成的角色人设描述"}

# 修改 get_characterglm_response 函数，使其能够接受两个角色的人设
def get_characterglm_response(dialogue_history, meta_a, meta_b):
    # 这里应该是调用 CharacterGLM API 的逻辑，根据 dialogue_history 和两个角色的人设生成回复
    # 由于我们无法访问实际的 API，这里只是返回一个模拟的回复
    return "模拟回复"

# 添加一个函数来保存对话数据到文件
def save_dialogue_to_file(dialogue_history, filename):
    # 将对话数据格式化为 JSON
    dialogue_data = [{"role": msg["role"], "content": msg["content"]} for msg in dialogue_history]
    # 将 JSON 数据写入文件
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(dialogue_data, file, ensure_ascii=False, indent=4)

# Streamlit 应用的主函数
def main():
    # ... (其他 Streamlit 应用代码保持不变)

    # 添加一个按钮来触发对话数据生成
    if st.button("生成对话数据"):
        # 基于用户输入的文本生成角色人设
        text = st.text_area("输入文本以生成角色人设")
        if text:
            profile_a = generate_character_profile(text)
            profile_b = generate_character_profile(text)  # 假设我们为两个角色生成相似的人设

            # 初始化对话历史
            dialogue_history = []

            # 交替生成回复
            for _ in range(5):  # 示例：生成5轮对话
                response = get_characterglm_response(dialogue_history, profile_a, profile_b)
                dialogue_history.append({"role": "character_a", "content": response})
                response = get_characterglm_response(dialogue_history, profile_b, profile_a)
                dialogue_history.append({"role": "character_b", "content": response})

            # 将生成的对话数据保存到文件
            filename = "dialogue_data.json"
            save_dialogue_to_file(dialogue_history, filename)
            st.success(f"对话数据已保存到 {filename}")

# 运行 Streamlit 应用
if __name__ == "__main__":
    main()
