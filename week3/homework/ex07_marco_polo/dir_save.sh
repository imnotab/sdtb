marco(){
    export SAVED_PWD=$(pwd)
}
polo(){
    cd "${SAVED_PWD:-.}" || echo "保存的目录不存在!"
}
