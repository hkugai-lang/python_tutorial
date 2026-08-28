# プログラムの実行ブロック
if __name__  == '__main__':
    # 変動値を3にしておく
    point = 3
    # LuckyResponderのオブジェクトを生成
    responder = LuckyResponder()
    # 変動値を設定してresponse()メソッドを実行
    res = responder.response(point)
    # 戻り値を表示
    print(res)
    
    # DrawResponderのオブジェクトを生成
    responder = DrawResponder()
    # 変動値を設定してresponse()メソッドを実行
    res = responder.response(point)
    # 戻り値を表示
    print(res)

    # BadResponderのオブジェクトを生成
    responder = BadResponder()
    # 変動値を設定してresponse()メソッドを実行
    res = responder.response(point)
    # 戻り値を表示
    print(res)
