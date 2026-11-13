import face_recognition 
import cv2
from ament_index_python.packages import get_package_share_directory 

def main():
    #获取图片的真实路径
    default_image_path = get_package_share_directory('demo_python_service')+'/resource/default.jpg'
    print(f"图片的真实路径：{default_image_path}")
    #使用cv2来加载图片
    image = cv2.imread(default_image_path)

    if image is None:
       print(f"错误：无法读取图像，请检查路径：{default_image_path}")
       return # 或 raise Exception
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    #检测人脸
    face_locations = face_recognition.face_locations(rgb_image,number_of_times_to_upsample=1,
    model= 'hog')
    #绘制人脸框
    for top,right,bottom,left in face_locations:
        cv2.rectangle(image,(left,top),(right,bottom),(255,0,0),4)
    #结果显示
    cv2.imshow('Face Detecte Result',image)
    cv2.waitKey(0) 
    cv2.destroyAllWindows()