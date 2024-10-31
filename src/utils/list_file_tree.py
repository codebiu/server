from pathlib import Path
import json

def build_directory_tree(root_path, tree=None):
    if tree is None:
        tree = {}
    root = Path(root_path)
    for entry in root.iterdir():
        if entry.is_dir():
            # 如果是目录，则递归构建子树
            tree[entry.name] = build_directory_tree(entry, {})
        else:
            # 如果是文件，则直接添加到树中
            tree[entry.name] = None
    return tree

if __name__ == "__main__":
    current_dir = Path.cwd()  # 获取当前工作目录
    directory_tree = build_directory_tree(current_dir)
    # 将目录树转换为 JSON 格式
    json_tree = json.dumps(directory_tree, indent=2, ensure_ascii=False)
    print(json_tree)