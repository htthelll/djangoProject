// 获取文件输入框和上传按钮的元素
const fileInput = document.getElementById('image-input');
const uploadButton = document.getElementById('uploadButton');

// 监听文件选择事件
fileInput.addEventListener('change', () => {
  if (fileInput.files.length > 0) {
    uploadButton.style.display = 'block';
    uploadButton.style.marginTop = '30px';
    uploadButton.style.marginLeft = 'auto';
    uploadButton.style.marginRight = 'auto';
  } else {
    uploadButton.style.display = 'none'; // 隐藏上传按钮
  }
});
