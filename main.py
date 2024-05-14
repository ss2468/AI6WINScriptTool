from ai6win_mes_gui import AI6WINMesGUI

debug = False

def test(mode: str):
    from ai6win_mes import AI6WINScript

    base_name = ""
    script_mes = "{}.mes".format(base_name)
    file_txt = "{}.txt".format(base_name)

    if mode == "diss":
        new_script = AI6WINScript(script_mes, file_txt, verbose=True, debug=False, version=1)
        new_script.disassemble()
        del new_script
    elif mode == "ass":
        new_script = AI6WINScript(script_mes, file_txt, verbose=True, debug=False)
        new_script.assemble()
        del new_script
    elif mode == "diss_for_hack":
        new_script = AI6WINScript(script_mes, file_txt, verbose=True, debug=True, hackerman_mode=True)
        new_script.disassemble()
        del new_script

def main():
    AI6WINMesGUI()
    return True

if __name__ == '__main__':
    # if debug:
    #     test("diss")
    # else:
    #     main()

    from ai6win_mes import AI6WINScript
    import os

    def find_suffix(dir, suffixs):
        allfiles = []
        for i in suffixs:
            files = [
                dir + "/" + j for j in os.listdir(dir)
                if os.path.isfile(os.path.join(dir, j)) and j.endswith(i)
            ]
            allfiles.extend(files)
        return allfiles

    # 批量拆包
    path = "C:/Users/Administrator/UntitledProjects/test/mes"
    files = find_suffix(path, ["mes"])
    for i in files:
        base_name = i.replace(".mes", "")
        script_mes = "{}.mes".format(base_name)
        file_txt = "{}.txt".format(base_name)
        new_script = AI6WINScript(script_mes, file_txt, verbose=True, debug=False, version=1)
        new_script.disassemble()

    # # 批量打包
    # # 打包可能出现编码问题，搜索cp932或SHIFT_JISX0213
    # path = "C:/Users/Administrator/UntitledProjects/test/txt"
    # files = find_suffix(path, ["txt"])
    # for i in files:
    #     base_name = i.replace(".txt", "")
    #     script_mes = "{}.mes".format(base_name)
    #     file_txt = "{}.txt".format(base_name)
    #     new_script = AI6WINScript(script_mes, file_txt, verbose=True, debug=False, version=1)
    #     new_script.assemble()
