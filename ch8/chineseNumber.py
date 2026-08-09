def number_to_chinese (num):
    if num==0:
        return '零'
    tupNumberals=('零','壹','貳','叁','肆','伍','陸','柒','捌','玖')
    tupUnits=('','拾','佰','仟','萬')

    tupNum=tuple(str(num))
    length=len(tupNum)
    result=''
    i=0
    for digit in tupNum:
        digit=int(digit)
        if digit!=0:
            result+=tupNumberals[digit]+tupUnits[length-i-1]
        else:
            if i>0 and tupNum[i-1] == '0':
                result=result+tupNumberals[digit]
        i+=1
    return result.rstrip('零')

input_num = int(input('請輸入5位數字以下數值 '))
output_chinese=number_to_chinese(input_num)
print(f'數字 {input_num} 的中文表示為: {output_chinese}')