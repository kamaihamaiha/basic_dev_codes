package com.kk.utils;

import java.util.ArrayList;
import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class StringHelper {

    public static String filterHtml(String str) {
        if (str == null) return "";
        str = str.replace("&nbsp;", " ");
        str = str.replace("&lt;", " ");
        str = str.replace("&gt;", " ");
        str = str.replace("<BR>", "\r\n");
        str = str.replace("<BR />", "\r\n");
        str = str.replace("<br>", "\r\n");
        str = str.replace("<br />", "\r\n");
        str = str.replace("</td>", "\t ");
        str = str.replace("</tr>", "\r\n");
        str = str.replace("<span", "\r\n<span");
        str = str.replace("<div", "\r\n<div");
        str = str.replace("</div>", "\r\n");
        str = str.replace("<li>", "\r\n- ");
        str = str.replace("</p>", "\r\n");
        str = str.replace("<p>", "\r\n");
        str = str.replaceAll("\\r+", "\n").replaceAll("\\n+", "\n");
        String regex = "<.*?>";
        return str.replaceAll(regex, "");
    }

    public static void list2arrayDemo(){
        List<String> list = new ArrayList<>();
        list.add("one");
        list.add("two");
        list.add("three");
        list.add("four");

        String[] numArray = list.toArray(new String[0]);
        for (String s : numArray) {
            System.out.println(s);
        }
    }

    public static String highLightWord(String sentence, String key){
        // Allergens are anything harmless (or neutral) that can be inhaled in air by nose and trigger excessive immune reaction.
        // allergen
        String hexColor = "#FF0000";
        if (sentence.contains("<span")) {
            return sentence.replace("<span", String.format("<span style='color:%s' ", hexColor));
        } else if (sentence.contains(key.concat(key))) {
            return sentence.replace(key, String.format("<span style='color:%s'>%s</span>", hexColor, key));
        } else if (sentence.contains(word2Cap(key))) {
            return sentence.replace(word2Cap(key), String.format("<span style='color:%s'>%s</span>", hexColor, word2Cap(key)));
        }
        return sentence;
    }


    /**
     * 转化成大些字母
     * @param character
     * @return
     */
    private Character letter2Capital(Character character) {
        char c = character;
        // 小写字母范围
        if (c >= 97 && c <= 122) {
            c = (char) (c - 32);
        }
        return c;
    }

    public static String word2Cap(String word){
//        if (TextUtils.isEmpty(word)) return word;

        char startC = word.charAt(0);
        char targetC = startC;
        if (startC >= 97 && startC <= 122) {
            // 小写字母开头
            targetC = (char) (startC - 32);
            return word.toLowerCase().replace(startC, targetC);
        }
        return word;
    }

    private static List<String> filterHtmlImgTag(String source){
        List<String> target = new ArrayList<>();
        if (source != null && !source.isEmpty()) {
            Pattern pattern = Pattern.compile("<img.*?src\\s*=\\s*\"(.*?)\".*?>"); // ios
            Matcher matcher = pattern.matcher(source);
            while (matcher.find()) {
                System.out.println("匹配了");
                target.add(matcher.group());
            }
        }
        return target;
    }

    /**
     * 获取HTML文件里面的IMG标签的SRC地址
     * @param htmlText 带html格式的文本
     */
    public static List<String> getHtmlImageSrcList(String htmlText) {
        List<String> imgSrc = new ArrayList<String>();
        Matcher m = Pattern.compile("src=\"?(.*?)(\"|>|\\s+)").matcher(htmlText);
        while (m.find()) {
            imgSrc.add(m.group(1));
        }
        return imgSrc;
    }

    public static List<String> getHtmlImageSrcListGroup(String htmlText) {
        List<String> imgSrc = new ArrayList<String>();
        Matcher m = Pattern.compile("src=\"?(.*?)(\"|>|\\s+)").matcher(htmlText);
        while (m.find()) {
            imgSrc.add(m.group());
        }
        return imgSrc;
    }

    public static String getLinkFormat(String link){
        StringBuilder sb = new StringBuilder();
        sb.append("<a href=\"");
        sb.append(link);
        sb.append("\">");
        sb.append("[图片]");
        sb.append("</a>");
        return sb.toString();
    }


    public static void main(String[] args) {

        // 替换成：<a href="https://files.kf5.com/attachments/download/10434/13714718/00162eb887797f4b7729a632e41f7bb/">[图片]</a>
//        String testImg = "<img src=\"https://files.kf5.com/attachments/download/10434/13714718/00162eb887797f4b7729a632e41f7bb/\" alt=\"ScreenShot-2022-08-04-at-08.50.16.png\">";
        String testMsg = "您好，\n" +
                "如果您在安卓平板中遇到了下图所示的情况（图一/图二）：\n" +
                "对于华为平板，在系统设置中搜索“平行视界”，关闭欧路词典的这个选项（图三），就会恢复正常;\n" +
                "对于小米平板, 相关设置的名称是“横屏模式”， 同样在系统设置中检索关闭即可；\n" +
                "其他品牌的平板操作逻辑一致，但设置项名称可能会有不同。\n" +
                "<img src=\"https://files.kf5.com/attachments/download/10434/12969600/001621735daa3f4714c787b5a612034/\" title=\"\" alt=\"图片.png\"><img src=\"https://files.kf5.com/attachments/download/10434/13530681/00162b436e2512ae59d837216ac6592/\" title=\"\" alt=\"Screenshot_2022-06-23-17-46-47-142_com.eusoft.eud.jpg\">\n" +
                "<img src=\"https://files.kf5.com/attachments/download/10434/12969614/001621736542760352f522f8b6f1627/\" title=\"\" alt=\"图片.png\">";

        String target = testMsg;
        List<String> htmlImgTags = filterHtmlImgTag(testMsg);
        for (String htmlImgTag : htmlImgTags) {
            System.out.println("提取 img 标签：" + htmlImgTag);
        }

        List<String> htmlImageSrcList = getHtmlImageSrcList(testMsg);

        if (htmlImgTags.size() == htmlImageSrcList.size()) {
            for (int i = 0; i < htmlImgTags.size(); i++) {
                String linkFormat = getLinkFormat(htmlImageSrcList.get(i)) + "\n";
                System.out.println("格式化 img 标签: " + linkFormat);

                // 替换
                target = target.replace(htmlImgTags.get(i), linkFormat);
            }
        }

        System.out.println("result: " + target);
    }
}
