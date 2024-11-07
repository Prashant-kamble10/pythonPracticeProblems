// 1 = find the longest word from the string

function sample(str){
    arr =  str.split(" ")

    var longestWord = ""
    for(i=0; i < arr.length; i++){
        if(arr[i].length > longestWord.length){
            longestWord = arr[i]
        }
    }
    console.log(longestWord)
}

sample("my name is prashant kamble")



