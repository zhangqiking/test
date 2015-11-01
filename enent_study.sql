--该段程序的功能为将原始数据规范化并作数据清洗

declare @j int
set @j=1
declare @file_num int
declare @temp char(10)            --temp为新表名称
declare @temp3 char(10)           --temp为旧表名称
select @file_num=max(FileID) from files
while @j<=@file_num
   begin
       select @temp=sheet_name from newfiles where  newfileID=@j
       select @temp3=sheet_name from files where  FileID=@j
       exec('create table ' +@temp+ '(ID int identity(1,1) not null, 名称 char(10),价格 float,交易量 float)')   --使用变量名动态创建表
       exec('select * into ##tem from ' +@temp3)                                                                --用一个临时表将数据复制到新的数据表中
       exec('insert into ' +@temp+'(名称,价格,交易量) select 名称,价格,交易量 from ##tem')
       drop table ##tem                                                                                         --删除全局临时表
       set @j=@j+1
       exec('delete from ' + @temp+ ' where 交易量 is null')
   end
        
   
        

--该段程序的功能是计算每支股票的收益率


declare @i int
declare @n int
declare @temp1 float                                    --保存第i支股票价格
declare @temp2 float                                    --保存第i+1支股票价格
declare @sheet_name char(10)
declare @para_1 nvarchar(100)
declare @para_2 nvarchar(100)

declare @para_4 nvarchar(500)
declare @sql_4 nvarchar(500)

declare @sql_1 nvarchar(100)
declare @sql_2 nvarchar(100)

declare @result float

declare @maxID int
declare @ID int
set @ID=1
select @maxID=MAX(newfileID) from newfiles
print @maxID
while @ID<=@maxID
   begin
       select @sheet_name=sheet_name from newfiles where  newfileID=@ID
       exec('alter table ' +@sheet_name+ ' add shouyi decimal(18,4) not NULL default(0)')
       declare @sql nvarchar(1000)
       set @sql = 'select @n=max(ID) ' + ' from ' +@sheet_name
       exec sp_executesql @sql,N'@n int output',@n output
       print @n
       set @i=1
       while @i<=@n
       begin
        
         set @sql_1 = N'select @temp_out_1=价格 ' + ' from ' +@sheet_name+ 'where ID=@tem'
         set @sql_2 = N'select @temp_out_2=价格 ' + ' from ' +@sheet_name+ 'where ID=@tem+1'
         set @para_1 = N'@tem NVARCHAR(20),@temp_out_1 float output'
         set @para_2 = N'@tem NVARCHAR(20),@temp_out_2 float output'
         
         exec sp_executesql @sql_1,
                   @para_1,
                   @tem=@i,
                   @temp_out_1=@temp1 output;
                  
                   
          exec sp_executesql @sql_2,
                             @para_2,
                             @tem=@i,
                             @temp_out_2=@temp2 output;
                   
         
         set @result=(@temp2-@temp1)/@temp1
         print @result
         set @sql_4 =N'update ' +@sheet_name+ 'set shouyi=@r where ID=@tem+1'
         set @para_4 = N'@tem NVARCHAR(20),@r float'
         exec sp_executesql @sql_4,
                            @para_4,
                            @tem=@i,
                            @r=@result;
         set @i=@i+1
     end
     set @ID=@ID+1
end












/*
--动态语言中给变量赋值的方法
declare @n nvarchar(10)
declare @sql nvarchar(1000)
declare @temp nvarchar(10)
select @temp=sheet_name from newfiles where  newfileID=1
set @sql = 'select @n=max(ID) ' + ' from ' +@temp
exec sp_executesql @sql,N'@n int output',@n output
print @n
*/


                      
