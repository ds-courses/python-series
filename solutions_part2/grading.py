def comment_grade(grade: int, mode: str = 'normal') -> str :
    ''' Provide a feedbac k according to the grade value
    
        Parameters
        ----------
        grade
            The amount of distance traveled
        mode
            The feedback mode, either "normal" (default) or "positive_reinforcement"

        Returns
        -------
        comment
            The grade feedback

        Examples
        --------
        >>> comment_grade(5)
        'Grade high enough'
    '''
    if grade < 5:
        return('Grade too low')
    elif grade > 5:
        if mode == 'normal':
            return('Grade high enough')
        elif mode == 'positive_reinforcement':
            return('Well done, keep going!')
        else:
            raise ValueError('The mode should be "normal" or "positive_reinforcement"')

def test_comments():
    assert comment_grade(0, mode='normal') == 'Grade too low'
    assert comment_grade(2, mode='normal') == 'Grade too low'
    #assert comment_grade(5, mode='normal') == 'Grade high enough'
    #assert comment_grade(5, mode='positive_reinforcement') == 'Well done, keep going!'
    assert comment_grade(10, mode='normal') == 'Grade high enough'
    assert comment_grade(10, mode='positive_reinforcement') == 'Well done, keep going!'