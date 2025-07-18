from project import questions,choose_answer,update_score,exit_score
def main():
    test_questions()
    test_choose_answer()
    test_update_score()
    test_exit_score()
def test_questions():
    questions_list,correct_options=questions()
    assert isinstance(questions_list,list),"questions_list should be a list"
    assert isinstance(correct_options,list),"correct_options should be a list"
    assert len(questions_list)==len(correct_options),"Length of questions_list and correct_options should be equal"
    print("test_questions passed!")
def test_choose_answer():
    assert choose_answer('A','A')==True,"choose_answer should return True for correct answer"
    assert choose_answer('A','B')==False,"choose_answer should return False for incorrect answer"
    print("test_choose_answer passed!")
def test_update_score():
    score=0
    score=update_score(score,True,1)
    assert score==1,"update_score should increment score for currect answer"
    score=update_score(score,False,2)
    assert score==1,"update_score should not change score for increment answer"
    print("test_update_score passed!")
def test_exit_score():
    assert exit_score(3,5)==None,"exit_score should return None"
    print("test_exit_score passed!")
if __name__="__main__":
    main()



